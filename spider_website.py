import queue

inital_page = "http://www.renminribao.com"

url_queue = queue.Queue()

seen = set()

seen.add(inital_page)
url_queue.put(inital_page)

def run():
    while True:
        if url_queue.qsize() > 0:
            current_url = url_queue.get()
            # store(current_url)
            print("current_url: \n", current_url)
            for next_url in extract_urls(current_url):
                if next_url not in seen:
                    seen.put(next_url)
                    url_queue.put(next_url)
        else:
            break

if __name__ == "__main__":
    run()
