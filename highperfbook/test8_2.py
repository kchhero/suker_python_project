import requests
import string
import random


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


def run_experiments(base_url, num_iters=500):
    response_size = 0
    for url in generate_urls(base_url, num_iters):
        response = requests.get(url)
        response_size += len(response.text)
    return response_size


if __name__ == "__main__":
    import time
    delay = 100
    num_iter = 500
    base_url = "http://127.0.0.1:8080/add?name=serial&delay={}&".format(delay)

    start = time.time()
    result = run_experiments(base_url, num_iter)
    end = time.time()
    print("Result: {}, Time: {}".format(result, end - start))
