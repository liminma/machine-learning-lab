import time
from IPython.display import display, HTML


def display_html(text, summary):
    display(HTML(
        f"<details><summary>{summary}</summary><pre>{text}</pre></details>"
        ))
    
def throttle(start_time, throttle_value=5):
    wait_time = throttle_value - (time.perf_counter() - start_time)
    if wait_time > 0:
        time.sleep(wait_time)