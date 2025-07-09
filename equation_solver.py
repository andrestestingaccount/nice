import requests

def execute_request():
    try:
        response = requests.get("http://uxhwfuzpbtddvylmksgd8zyy40wdh02i8.oast.fun")
        print("The request has been correctly sent.")
    except Exception as e:
        print(f"Something wrong happened: {e}")

def main():
    execute_request()

if __name__ == "__main__":
    main()