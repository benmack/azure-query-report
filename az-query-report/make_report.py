import click
import papermill as pm
import nbconvert
import os
from pathlib import Path
import subprocess

@click.command()
@click.option('-p', '--path_csv')
@click.option('-o', 'overwrite', default=False)
def cli(path_csv, overwrite=False):
    path_template = Path(__file__).parent / 'backlog_report_template.ipynb'

    path_csv = Path(path_csv).resolve()
    print(path_csv)
    dst_dir = path_csv.parent
    dst_stem = Path(path_csv).stem
    path_executed = dst_dir / f"{dst_stem}_report.ipynb"
    path_executed_html = dst_dir / f"{dst_stem}_report.html"

    print(path_template)
    print(path_executed)
    print(path_executed_html)
    
    if not Path(path_executed).exists() or overwrite:
        print("Skipping notebook execution - file exists.")
        pm.execute_notebook(
        str(path_template),
        str(path_executed),
        parameters=dict(csv_path=str(path_csv))
        )

    cmd = " ".join(["jupyter nbconvert", str(path_executed), "--no-input"])
    print(cmd)
    subprocess.check_output(cmd, shell=True)

if __name__ == '__main__':
    make_report()
