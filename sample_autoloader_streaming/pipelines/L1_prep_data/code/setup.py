from setuptools import setup, find_packages
setup(
    name = 'L1_PrepData_FirstBatch',
    version = '1.0',
    packages = find_packages(include = ('l1_prep_data*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.6.2'],
    entry_points = {
'console_scripts' : [
'main = l1_prep_data.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
