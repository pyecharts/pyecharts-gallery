import os

FILTER_DIR = [".idea", ".git", ".mypy_cache"]


def run_command(command: str):
    try:
        os.system(command)
        print("Execute {} is success!".format(command))
    except Exception as err:
        print(err)


def run_black_format_code():
    run_command(command="black .")


def run_flake_8_check():
    run_command(command="flake8 --max-line-length 89 --ignore=F401")


def run_all_charts(path: str):
    charts_path = sorted(os.listdir(path))[5:]
    for chart_path in charts_path:
        chart_path = os.path.join(path, chart_path)
        if os.path.isdir(chart_path):
            for test_chart_path in os.listdir(chart_path):
                if ".py" in test_chart_path:
                    os.chdir(chart_path)
                    test_chart_path = os.path.join(chart_path, test_chart_path)
                    run_command(command="python3 {}".format(test_chart_path))
                    print(
                        "Render {} chart success! \n {}".format(
                            test_chart_path, "#" * 100
                        )
                    )


if __name__ == "__main__":
    run_black_format_code()
    run_flake_8_check()
    run_all_charts(path=os.getcwd())
