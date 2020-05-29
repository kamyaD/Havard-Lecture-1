import requests

def main():
    base = input("First Currency:")
    other = input("Second Currency: ")

    res = requests.get("http://data.fixer.io/api/latest?access_key=a5fc25d9192e15807a15410fae944c02&format=1", params={"base": base, "symbols": other})
    if res.status_code !=200:
        raise Exception("ERROR: API request unseccessful.")
    data = res.json()
    print(data)
    rate = data
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
