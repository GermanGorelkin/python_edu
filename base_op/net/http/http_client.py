import http.client


def main():
    conn = http.client.HTTPConnection(host="localhost", port=8000)
    conn.request("GET", "/")
    res = conn.getresponse()
    print(res.status, res.reason)
    for hd in res.headers.items():
        print(hd)
    res_body = res.read()
    print(res_body)
    conn.close()


if __name__ == "__main__":
    main()
