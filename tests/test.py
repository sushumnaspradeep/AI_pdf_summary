import requests

def test_api_summarization():
    url = "http://127.0.0.1:8000/summarize?model=bart"
    files = {"file": open("sample.pdf", "rb")}
    response = requests.post(url, files=files)

    assert response.status_code == 200
    assert "summary" in response.json()

if __name__ == "__main__":
    test_api_summarization()
