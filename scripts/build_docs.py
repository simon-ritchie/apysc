"""Documentations build script.

Command example:
$ python ./scripts/build_docs.py
"""

import hashlib
import multiprocessing as mp
import os
import re
import shutil
import subprocess as sp
import sys
from distutils.dir_util import copy_tree
from logging import Logger
from typing import Any
from typing import Dict
from typing import List
from typing import Match
from typing import Optional as Op

from typing_extensions import Final
from typing_extensions import TypedDict

sys.path.append('./')

from apysc._console import loggers
from apysc._jslib import jslib_util
from apysc._string import docstring_util

logger: Logger = loggers.get_info_logger()

_jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
_jslib_file_name_keys_dict: Dict[str, Any] = {
    jslib_file_name: None for jslib_file_name in _jslib_file_names}


def _main() -> None:
    """Entry point of this command.
    """
    print('-' * 20)
    logger.info(msg='Documentation build started...')

    _exec_document_lint_and_script()

    logger.info(msg='Sphinx build command started...')
    complete_process: sp.CompletedProcess = sp.run(
        'sphinx-build ./docs_src/source/ ./docs/', shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    print(stdout)
    _move_and_adjust_updated_files()

    logger.info(msg='Build completed!')


def _remove_runnable_inline_comment_from_code_blocks(
        dir_path: str = './docs/') -> None:
    """
    Remove `# runnable` inline comment from each exported documents'
    code blocks recursively.

    Parameters
    ----------
    dir_path : str, default './docs/'
        Target directory path.
    """
    from apysc._string import string_util
    RUNNABLE_COMMENT_CODE: Final[str] = (
        r'<span></span><span class="c1"># runnable</span>'
    )
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if file_or_dir_name == 'static' or file_or_dir_name == '_static':
            continue
        if os.path.isdir(file_or_dir_path):
            _remove_runnable_inline_comment_from_code_blocks(
                dir_path=file_or_dir_path)
            continue
        if not file_or_dir_path.endswith('.html'):
            continue
        string_util.substitute_file_by_pattern(
            file_path=file_or_dir_path,
            pattern=RUNNABLE_COMMENT_CODE,
            repl='',
            flags=re.MULTILINE)


class _ScriptData(TypedDict):
    md_file_path: str
    hashed_val: str
    runnable_script: str


class _RunReturnData(TypedDict):
    md_file_path: str
    runnable_script: str
    stdout: str


def _exec_document_lint_and_script(
        limit_count: Op[int] = None) -> List[str]:
    """
    Execute each runnable scripts in the documents and check with
    each lint.

    Parameters
    ----------
    limit_count : int or None, optional
        Limitation of the script execution count.

    Returns
    -------
    executed_scripts : list of str
        List of executed Python scripts.
    """
    from apysc._file import file_util
    md_file_paths: List[str] = \
        file_util.get_specified_ext_file_paths_recursively(
            extension='.md', dir_path='./docs_src/')
    workers: int = mp.cpu_count()

    with mp.Pool(workers) as p:
        logger.info(
            msg='Removing document hash files if docstring source '
                'files have been modified...')
        docstring_module_paths: List[List[str]] = p.map(
            func=_remove_document_hash_files_if_docstring_src_modified,
            iterable=md_file_paths)
        docstring_module_paths_: List[str] = \
            _flatten_2dim_module_paths_and_make_it_unique(
                docstring_module_paths=docstring_module_paths)

        logger.info(msg='Saving docstring modules hash files...')
        p.map(
            func=_save_docstring_module_hash,
            iterable=docstring_module_paths_)

        logger.info(msg='Slicing not updated markdown files...')
        markdown_data_list_: List[Op[_MarkdownData]] = p.map(
            func=_convert_path_to_markdown_data_with_hashed_val,
            iterable=md_file_paths)
        markdown_data_list: List[_MarkdownData] = \
            _remove_none_from_markdown_data_list(
                markdown_data_list=markdown_data_list_)
        script_data_list: List[_ScriptData] = _make_script_data_list(
            markdown_data_list=markdown_data_list,
            limit_count=limit_count)

        logger.info(msg="Document's code block flake8 checking started...")
        p.map(func=_check_code_block_with_flake8, iterable=script_data_list)
        logger.info(
            msg="Document's code block numdoclint checking started...")
        p.map(
            func=_check_code_block_with_numdoclint, iterable=script_data_list)
        logger.info(msg="Document's code block mypy checking started...")
        p.map(func=_check_code_block_with_mypy, iterable=script_data_list)

        logger.info(msg="Document's scripts execution started...")
        run_return_data_list: List[_RunReturnData] = p.map(
            func=_run_code_block_script, iterable=script_data_list)

        logger.info(
            msg="Replacing docstring path specification in documents...")
        p.map(
            func=_replace_docstring_specification,
            iterable=markdown_data_list)
    _move_code_block_outputs()
    _validate_script_return_data(return_data_list=run_return_data_list)

    _save_hashed_val(script_data_list=script_data_list)
    executed_scripts: List[str] = [
        script_data['runnable_script'] for script_data in script_data_list]
    return executed_scripts


def _save_docstring_module_hash(module_path: str) -> None:
    """
    Save a docstring module hash file.

    Parameters
    ----------
    module_path : str
        Target module path.
    """
    from apysc._lint_and_doc import lint_and_doc_hash_util
    lint_and_doc_hash_util.save_target_module_hash(
        module_path=module_path,
        hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_SRC)


def _flatten_2dim_module_paths_and_make_it_unique(
        *, docstring_module_paths: List[List[str]]) -> List[str]:
    """
    Flatten a specified 2-dimensional docstring module paths
    list and make it unique.

    Parameters
    ----------
    docstring_module_paths : list of list
        Target 2-dim module paths list.

    Returns
    -------
    flattened_module_paths : list of str
        Flattened module paths list.
    """
    flattened_module_paths: List[str] = []
    for docstring_module_paths_ in docstring_module_paths:
        flattened_module_paths.extend(docstring_module_paths_)
    flattened_module_paths = list(set(flattened_module_paths))
    return flattened_module_paths


def _remove_document_hash_files_if_docstring_src_modified(
        md_file_path: str) -> List[str]:
    """
    Remove docstring hash files if docstring sources have
    been modified.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    module_paths : list of str
        Target docstring module paths in a specified markdown.
    """
    from apysc._lint_and_doc import lint_and_doc_hash_util
    from apysc._file import file_util
    module_paths: List[str] = docstring_util.get_docstring_src_module_paths(
        md_file_path=md_file_path)
    if not module_paths:
        return []
    for module_path in module_paths:
        saved_hash: str = lint_and_doc_hash_util.read_saved_hash(
            module_path=module_path,
            hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_SRC)
        current_hash: str = _read_file_and_hash_it(
            file_path=module_path)
        if saved_hash == current_hash:
            continue
        hash_file_path: str = _get_doc_hash_file_path(
            md_file_path=md_file_path)
        file_util.remove_file_if_exists(file_path=hash_file_path)
        break
    return module_paths


class _MarkdownData(TypedDict):
    md_file_path: str
    hashed_val: str


def _replace_docstring_specification(
        markdown_data: _MarkdownData) -> None:
    """
    Replace a markdown's docstring specification by the
    converted docstring text.

    Parameters
    ----------
    markdown_data : _MarkdownData
        Target markdown data.
    """
    docstring_util.reset_replaced_docstring_section(
        md_file_path=markdown_data['md_file_path'])
    docstring_util.replace_docstring_path_specification(
        md_file_path=markdown_data['md_file_path'])


def _remove_none_from_markdown_data_list(
        markdown_data_list: List[Op[_MarkdownData]]) -> List[_MarkdownData]:
    """
    Remove the None values from the specified markdown data list.

    Parameters
    ----------
    markdown_data_list : list of _MarkdownData or None
        Target list.

    Returns
    -------
    markdown_data_list_ : list of _MarkdownData
        The list after removing the None values.
    """
    markdown_data_list_: List[_MarkdownData] = []
    for markdown_data in markdown_data_list:
        if markdown_data is None:
            continue
        markdown_data_list_.append(markdown_data)
    return markdown_data_list_


_CODE_BLOCK_OUTPUT_DIR_PATH: str = './docs_src/source/_static/'


def _move_code_block_outputs(
        output_dir_path: str = _CODE_BLOCK_OUTPUT_DIR_PATH) -> None:
    """
    Move each created output by the code block script execution.

    Parameters
    ----------
    output_dir_path : str, default _CODE_BLOCK_OUTPUT_DIR_PATH
        Expected output root directory path.
    """
    code_block_outputs_dir_paths: List[str] = \
        _get_code_block_output_dir_paths(output_dir_path=output_dir_path)
    for src_dir_path in code_block_outputs_dir_paths:
        dst_dir_path: str = src_dir_path.replace(
            output_dir_path,
            './docs/static/',
            1,
        )
        copy_tree(src=src_dir_path, dst=dst_dir_path)
        shutil.rmtree(src_dir_path, ignore_errors=True)


def _get_code_block_output_dir_paths(
        output_dir_path: str = _CODE_BLOCK_OUTPUT_DIR_PATH) -> List[str]:
    """
    Get the created output directory paths by the code block script
    execution.

    Parameters
    ----------
    output_dir_path : str, default _CODE_BLOCK_OUTPUT_DIR_PATH
        Expected output root directory path.

    Returns
    -------
    dir_paths : list of str
        Target directory paths.
    """
    if not os.path.isdir(output_dir_path):
        return []
    file_or_dir_names: List[str] = os.listdir(output_dir_path)
    dir_paths: List[str] = []
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(
            output_dir_path, file_or_dir_name)
        if not os.path.isdir(file_or_dir_path):
            continue
        in_dir_file_or_dir_names: List[str] = os.listdir(file_or_dir_path)
        if in_dir_file_or_dir_names != ['index.html']:
            continue
        dir_paths.append(f'{file_or_dir_path}/')
    return dir_paths


class _CodeBlockMypyError(Exception):
    pass


def _check_code_block_with_mypy(script_data: _ScriptData) -> None:
    """
    Check a code block with the mypy.

    Parameters
    ----------
    script_data : _ScriptData
        Target script data.

    Raises
    ------
    _CodeBlockMypyError
        If there is a mypy error.
    """
    from apysc._file import module_util
    from scripts.apply_lints_and_build_docs import MYPY_NO_PATH_COMMAND
    from scripts.apply_lints_and_build_docs import run_command
    runnable_script: str = script_data['runnable_script']
    md_file_path: str = script_data['md_file_path']
    tmp_module_path: str = module_util.save_tmp_module(script=runnable_script)
    command: str = f'{MYPY_NO_PATH_COMMAND} {tmp_module_path}'
    stdout: str = run_command(command=command).strip()
    os.remove(tmp_module_path)
    if 'Success: no issues found' not in stdout:
        raise _CodeBlockMypyError(
            'There is a mypy error in the following document code block:'
            f'\nDocument path: {md_file_path}'
            f'\n Code block: \n\n{runnable_script}\n'
            f'\nmypy message: {stdout}')


class _CodeBlockNumdoclintError(Exception):
    pass


def _check_code_block_with_numdoclint(script_data: _ScriptData) -> None:
    """
    Check a code block with the numdoclint.

    Parameters
    ----------
    script_data : _ScriptData
        Target script data.

    Raises
    ------
    _CodeBlockNumdoclintError
        If there is a numdoclint error.
    """
    from apysc._file import module_util
    from scripts.apply_lints_and_build_docs import run_command
    runnable_script: str = script_data['runnable_script']
    md_file_path: str = script_data['md_file_path']
    tmp_module_path: str = module_util.save_tmp_module(script=runnable_script)
    command: str = (
        f'numdoclint -p {tmp_module_path} -f test,sample,_test,_sample')
    stdout: str = run_command(command=command).strip()
    stdout = stdout.replace('[]', '')
    os.remove(tmp_module_path)
    if stdout != '':
        raise _CodeBlockNumdoclintError(
            'There is a numdoclint error in the following document '
            'code block:'
            f'\nDocument path: {md_file_path}'
            f'\nCode block:\n\n{runnable_script}\n'
            f'\nnumdoclint message: {stdout}')


class _CodeBlockFlake8Error(Exception):
    pass


def _check_code_block_with_flake8(script_data: _ScriptData) -> None:
    """
    Check a code block with the flake8 lint.

    Parameters
    ----------
    script_data : _ScriptData
        Target script data.

    Raises
    ------
    _CodeBlockFlake8Error
        If there is a flake8 lint error.
    """
    from apysc._file import module_util
    from scripts.apply_lints_and_build_docs import FLAKE8_NO_PATH_COMMAND
    from scripts.apply_lints_and_build_docs import run_command
    runnable_script: str = script_data['runnable_script']
    md_file_path: str = script_data['md_file_path']
    tmp_module_path: str = module_util.save_tmp_module(script=runnable_script)
    command: str = f'{FLAKE8_NO_PATH_COMMAND},W292,E501 {tmp_module_path}'
    stdout: str = run_command(command=command).strip()
    os.remove(tmp_module_path)
    if stdout != '':
        raise _CodeBlockFlake8Error(
            'There is a flake8 error in the following document code block:'
            f'\nDocument path: {md_file_path}'
            f'\nCode block:\n\n{runnable_script}\n'
            f'\nflake8 message: {stdout}'
        )


def _save_hashed_val(script_data_list: List[_ScriptData]) -> None:
    """
    Save executed markdown script hashed values to the file.

    Parameters
    ----------
    script_data_list : list of _ScriptData
        Executed script data list.
    """
    for script_data in script_data_list:
        _save_md_hashed_val(
            md_file_path=script_data['md_file_path'],
            hashed_val=script_data['hashed_val'])


def _validate_script_return_data(
        return_data_list: List[_RunReturnData]) -> None:
    """
    Validate the returned data list whether there are no
    tracebacks in the stdout.

    Parameters
    ----------
    return_data_list : list of _RunReturnData
        Data list returned from the script execution.

    Raises
    ------
    Exception
        If there are any tracebacks in the stdout.
    """
    for return_data in return_data_list:
        stdout: str = return_data['stdout']
        if 'Traceback' in stdout:
            md_file_path: str = return_data['md_file_path']
            runnable_script: str = return_data['runnable_script']
            raise Exception(
                'Error occurred while executing the document codeblock.'
                f'\nMarkdown file path: {md_file_path}'
                '\n-------------------------'
                f'\nRun script:\n{runnable_script}'
                '\n-------------------------'
                f'\nStdout: {stdout}')


def _run_code_block_script(script_data: _ScriptData) -> _RunReturnData:
    """
    Run a specified code block script.

    Parameters
    ----------
    script_data : _ScriptData
        Target script data.

    Returns
    -------
    return_data : _RunReturnData
        Script execution result data.
    """
    from apysc._file import module_util
    runnable_script: str = script_data['runnable_script']
    md_file_path: str = script_data['md_file_path']
    logger.info(
        msg=(
            '\n\n-------------------------\n\n'
            f'Executing document script: \n{runnable_script}'))
    stdout: str = module_util.save_tmp_module_and_run_script(
        script=runnable_script)
    return_data: _RunReturnData = {
        'md_file_path': md_file_path,
        'runnable_script': runnable_script,
        'stdout': stdout,
    }
    return return_data


def _make_script_data_list(
        markdown_data_list: List[_MarkdownData],
        limit_count: Op[int]) -> List[_ScriptData]:
    """
    Make a script data list for the multiprocessing argument.

    Parameters
    ----------
    markdown_data_list : list of _MarkdownData
        Target markdown data list.
    limit_count : int or None
        Limitation of the script execution count.

    Returns
    -------
    script_data_list : list of _ScriptData
        A script data list for the multiprocessing argument.
    """
    count: int = 0
    is_limit: bool = False
    script_data_list: List[_ScriptData] = []
    for markdown_data in markdown_data_list:
        runnable_scripts: List[str] = _get_runnable_scripts_in_md_code_blocks(
            md_file_path=markdown_data['md_file_path'])
        for runnable_script in runnable_scripts:
            script_data_list.append({
                'md_file_path': markdown_data['md_file_path'],
                'hashed_val': markdown_data['hashed_val'],
                'runnable_script': runnable_script,
            })
            count += 1
            if limit_count is not None and count == limit_count:
                is_limit = True
                break
        if is_limit:
            break
    return script_data_list


def _save_md_hashed_val(md_file_path: str, hashed_val: str) -> None:
    """
    Save markdown hashed string value to file.

    Parameters
    ----------
    md_file_path : str
        Original markdown file path.
    hashed_val : str
        Hashed markdown text value.
    """
    from apysc._file import file_util
    hash_file_path: str = _get_doc_hash_file_path(
        md_file_path=md_file_path)
    file_util.save_plain_txt(txt=hashed_val, file_path=hash_file_path)


HASHED_VALS_DIR_PATH: str = './docs_src/hashed_vals/'


def _get_doc_hash_file_path(md_file_path: str) -> str:
    """
    Get a document hash file path.

    Parameters
    ----------
    md_file_path : str
        Target document markdown file path.

    Returns
    -------
    hash_file_path : str
        A document hash file path.
    """
    under_source_file_path: str = _get_md_under_source_file_path(
        md_file_path=md_file_path)
    hash_file_path: str = os.path.join(
        HASHED_VALS_DIR_PATH, under_source_file_path,
    )
    return hash_file_path


def _convert_path_to_markdown_data_with_hashed_val(
        md_file_path: str) -> Op[_MarkdownData]:
    """
    Convert the markdown path to the markdown data with
    hashed value.

    Notes
    -----
    If the specified markdown isn't updated, this function
    returns None.

    Parameters
    ----------
    md_file_path : str
        Markdown file path.

    Returns
    -------
    markdown_data : _MarkdownData or None
        Converted markdown data.
    """
    if '/hashed_vals/' in md_file_path:
        return None
    under_source_file_path: str = _get_md_under_source_file_path(
        md_file_path=md_file_path)
    hash_file_path: str = os.path.join(
        HASHED_VALS_DIR_PATH,
        under_source_file_path,
    )
    hash_file_dir_path: str = os.path.dirname(hash_file_path)
    os.makedirs(hash_file_dir_path, exist_ok=True)
    saved_hashed_val: str = _read_md_file_hashed_val_from_file(
        hash_file_path=hash_file_path)
    md_hashed_val: str = _read_file_and_hash_it(
        file_path=md_file_path)
    if saved_hashed_val == md_hashed_val:
        return None
    return {
        'md_file_path': md_file_path,
        'hashed_val': md_hashed_val,
    }


def _get_md_under_source_file_path(md_file_path: str) -> str:
    """
    Get a markdown file path under the source directory.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    under_source_file_path : str
        File path that under the document source directory,
        e.g., './doc_src/source/any/path.md' will be 'any/path.md'.
    """
    under_source_file_path: str = md_file_path.split('/source/', 1)[1]
    return under_source_file_path


def _read_file_and_hash_it(*, file_path: str) -> str:
    """
    Read a text file and hash its text.

    Parameters
    ----------
    file_path : str
        Target file path.

    Returns
    -------
    hashed_val : str
        Hashed string value.
    """
    from apysc._file import file_util
    txt: str = file_util.read_txt(file_path=file_path)
    hashed_val: str = hashlib.sha1(txt.encode()).hexdigest()
    return hashed_val


def _read_md_file_hashed_val_from_file(hash_file_path: str) -> str:
    """
    Read the markdown file hashed value from the saved file.

    Parameters
    ----------
    hash_file_path : str
        Target hash file path.

    Returns
    -------
    hashed_val : str
        Hashed string value. If file does not exist, then blank string
        will be returned.
    """
    from apysc._file import file_util
    if not os.path.exists(hash_file_path):
        return ''
    hashed_val: str = file_util.read_txt(file_path=hash_file_path)
    hashed_val = hashed_val.strip()
    return hashed_val


class _CodeBlock:

    code_type: str
    code: str
    runnable: bool

    def __init__(self, code_type: str, code: str, runnable: bool) -> None:
        """
        Code block data class.

        Parameters
        ----------
        code_type : str
            Code type (e.g., 'py', 'sql', '', or something else).
        code : str
            Code in the target code block.
        runnable : bool
            If runnable code block, this will be True.
        """
        self.code_type = code_type
        self.code = code
        self.runnable = runnable


def _get_runnable_scripts_in_md_code_blocks(md_file_path: str) -> List[str]:
    """
    Get runnable Python scripts in the markdown code blocks.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.

    Returns
    -------
    runnable_scripts : list of str
        Runnable Python scripts in code blocks.
        Code blocks with the `# runnable` inline comment
        at the begining of the block will be targeted.
    """
    from apysc._file.file_util import read_txt
    md_txt: str = read_txt(file_path=md_file_path)
    code_blocks: List[_CodeBlock] = _get_code_blocks_from_txt(md_txt=md_txt)
    runnable_scripts: List[str] = []
    for code_block in code_blocks:
        if code_block.code_type != 'py':
            continue
        if not code_block.runnable:
            continue
        code: str = code_block.code
        code = _replace_html_saving_export_path_by_doc_path(code=code)
        code = _append_js_lib_path_and_skip_settings(code=code)
        runnable_scripts.append(code)
    return runnable_scripts


def _append_js_lib_path_and_skip_settings(code: str) -> str:
    """
    Append JavaScript libraries exporting directory path
    setting (js_lib_dir_path) and skipping setting
    (skip_js_lib_exporting) arguments in the code.

    Parameters
    ----------
    code : str
        Target Python code.

    Returns
    -------
    code : str
        Settings appended code.
    """
    code = re.sub(
        pattern=(
            r'(save_overall_html\(.+?)\)'
        ),
        repl=r"\1,\n    js_lib_dir_path='../', skip_js_lib_exporting=True)",
        string=code,
        count=1,
        flags=re.MULTILINE | re.DOTALL)
    return code


def _replace_html_saving_export_path_by_doc_path(code: str) -> str:
    """
    Replace html saving interace's export path argument value
    in the code by document path.

    Parameters
    ----------
    code : str
        Target Python code.

    Returns
    -------
    code : str
        Replaced code. html saving interface argument,
        for example, `save_overall_html` `dest_dir_path`
        will be replaced by './docs_src/_static/<original_path>/'.
    """
    match: Op[Match] = re.search(
        pattern=(
            r"save_overall_html\(.*?dest_dir_path='(.+?)'\)"
        ),
        string=code,
        flags=re.MULTILINE | re.DOTALL)
    if match is None:
        return code
    original_path: str = match.group(1)
    while original_path.startswith('.'):
        original_path = original_path.replace('.', '', 1)
    if original_path.startswith('/'):
        original_path = original_path.replace('/', '', 1)
    if not original_path.endswith('/'):
        original_path += '/'

    code = re.sub(
        pattern=(
            r"(save_overall_html\(.*?dest_dir_path=).+?\)"
        ),
        repl=rf"\1'./docs_src/source/_static/{original_path}')",
        string=code, count=1,
        flags=re.MULTILINE | re.DOTALL)
    return code


def _get_code_blocks_from_txt(md_txt: str) -> List[_CodeBlock]:
    """
    Get code blocks from a markdown text.

    Parameters
    ----------
    md_txt : str
        Target markdown text.

    Returns
    -------
    code_blocks : list of _CodeBlock
        Code blocks in a markdown text.
    """
    is_code_block: bool = False
    code_block_line_num: int = 0
    lines: List[str] = md_txt.splitlines()
    code_type: str = ''
    code: str = ''
    runnable: bool = False
    code_blocks: List[_CodeBlock] = []
    for line in lines:
        if not is_code_block and line.startswith('```'):
            code_type = line.replace('```', '')
            code_type = code_type.split(':')[0]
            is_code_block = True
            continue
        if not is_code_block:
            continue
        if line.startswith('```'):
            code_blocks.append(_CodeBlock(
                code_type=code_type, code=code, runnable=runnable))
            is_code_block = False
            code_block_line_num = 0
            code = ''
            runnable = False
            continue
        code_block_line_num += 1
        if code_block_line_num == 1 and line == '# runnable':
            runnable = True
            continue
        if code != '':
            code += '\n'
        code += line
    return code_blocks


def _move_and_adjust_updated_files() -> None:
    """
    Move and adjust (remove unnecessary string, etc) updated files.
    """
    if os.path.isdir('./docs/_static/'):
        logger.info(
            msg='Replacing `_static` and `_images` paths by `static` '
                'and `images`...')
        _replace_static_path_recursively(dir_path='./docs/')
        logger.info(
            msg='Removing `# runnable` inline comment from code blocks...')
        _remove_runnable_inline_comment_from_code_blocks(
            dir_path='./docs/')
        logger.info(msg='Copying updated document files...')
        copy_tree(src='./docs/_static/', dst='./docs/static/')
        logger.info(msg='Removing unnecessary static files...')
        shutil.rmtree('./docs/_static/', ignore_errors=True)
    if os.path.isdir('./docs/_images/'):
        logger.info(msg='Copying document images...')
        copy_tree(src='./docs/_images/', dst='./docs/images/')
        logger.info(msg='Removing unnecessary image files...')
        shutil.rmtree('./docs/_images/', ignore_errors=True)


def _replace_static_path_recursively(dir_path: str) -> None:
    """
    Replace each files' `_static` paths by `static`.

    Parameters
    ----------
    dir_path : str
        Target directory path.
    """
    file_or_dir_names: List[str] = os.listdir(dir_path)
    file_extensions: List[str] = ['.html', '.js']
    for file_or_dir_name in file_or_dir_names:
        if file_or_dir_name in _jslib_file_name_keys_dict:
            continue
        if file_or_dir_name == 'static' or file_or_dir_name == '_static':
            continue
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            _replace_static_path_recursively(dir_path=file_or_dir_path)
            continue
        extension: str = os.path.splitext(file_or_dir_path)[1]
        if extension not in file_extensions:
            continue
        with open(file_or_dir_path) as f:
            file_txt: str = f.read()
        file_txt = file_txt.replace('_static', 'static')
        file_txt = file_txt.replace('_images', 'images')
        with open(file_or_dir_path, 'w') as f:
            f.write(file_txt)


if __name__ == '__main__':
    _main()
