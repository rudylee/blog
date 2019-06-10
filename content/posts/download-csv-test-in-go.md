+++
title = "Download CSV Test in Go"
date = "2018-06-23"
slug = "2018/06/23/download-csv-test-in-go"
Categories = ["Go"]
+++

In the project I am working on, I have to write a test for a function that download CSV from external website and store it locally. I am pretty new in Go so please let me know if I am doing it wrong.

The function is pretty simple, it uses the Go `net/http` package to send a `GET` request and `os` package to write the HTTP response to a local file. See the full code below:

```go
package main

import (
  "io"
  "log"
  "net/http"
  "os"
)

func main() {
  DownloadCSV("https://www.asx.com.au/asx/research/ASXListedCompanies.csv", "asx-companies.csv")
}

func DownloadCSV(url string, filename string) error {
  out, _ := os.Create(filename)
  defer out.Close()

  resp, err := http.Get(url)
  defer resp.Body.Close()

  if _, err := io.Copy(out, resp.Body); err != nil {
    log.Fatal(err)
  }

  return err
}
```

The function we want to test is `DownloadCSV` which expects two arguments. `url` is a URL endpoint that host the CSV and `filename` is the name of local file to store the HTTP response.

There are three things I want to test here:

1. `http.Get` shouldn't return an error
2. It should create a local CSV file
3. The content of the local CSV file should match with the server

## `http.Get` shouldn't return an error

To test the first one, we will use an awesome Go package called `net/http/httptest`. This package allows us to create a HTTP server and set the response to whatever you want.

In the code below, you can see we start with creating the server which return a 200 response status ( line 10 - 12 ). After that, we pass the URL of the server to the `DownloadCSV` function and also the required filename. 

At the end, we do the assertion to make sure the function does not return an error. We are using Go testing package `Errorf` method to output the message if the assertion fail. This is important because we need it to mark the test as `FAIL`.

```go
package main

import (
  "net/http"
  "net/http/httptest"
  "testing"
)

func TestDownloadCSV(t *testing.T) {
  ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
  }))
  defer ts.Close()

  file := "test.csv"
  err := DownloadCSV(ts.URL, file)

  if err != nil {
    t.Errorf("Shouldn't have received an error, got %s", err)
  }
}
```

## It should create a local CSV file

We are going to use the `os` package to check the file existence and delete it after the test finished. Three functions we will use are  `Stat`, `IsNotExist` and `Remove`. `Stat` and `IsNotExists` are used to assert the file existence and `Remove` will clean up the file after test finished. 

```go
package main

import (
  "net/http"
  "net/http/httptest"
  "os"
  "testing"
)

func TestDownloadCSV(t *testing.T) {
  ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
  }))
  defer ts.Close()

  file := "test.csv"
  err := DownloadCSV(ts.URL, file)

  if err != nil {
    t.Errorf("Shouldn't have received an error, got %s", err)
  }

  if _, err := os.Stat(file); os.IsNotExist(err) {
    t.Errorf("Should have created a CSV file")
  }

  os.Remove(file)
}
```

## The content of the local CSV file should match with the server

The simplest way to do this test is to configure the `httptest` server to return a string and check if that string exists in the test file. We can take this a bit further by using an actual CSV file.

We can use test fixture to achieve this. We will create a new folder called `testdata`, put a CSV file inside it, set the `httptest` server to read the file using `ioutil.ReadFile` and return the content to the client. We will also use `ioutil.ReadFile` to do the assertion to compare the content of the files. Here is the final version of the test:

```go
package main

import (
  "bytes"
  "io/ioutil"
  "net/http"
  "net/http/httptest"
  "os"
  "testing"
)

func TestDownloadCSV(t *testing.T) {
  test_csv, _ := ioutil.ReadFile("testdata/asx-companies.csv")

  ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    w.Write(test_csv)
  }))
  defer ts.Close()

  file := "test.csv"
  err := DownloadCSV(ts.URL, file)

  if err != nil {
    t.Errorf("Shouldn't have received an error, got %s", err)
  }

  if _, err := os.Stat(file); os.IsNotExist(err) {
    t.Errorf("Should have created a CSV file")
  }

  expected, _ := ioutil.ReadFile(file)

  if !bytes.Equal(test_csv, expected) {
    t.Errorf("CSV file should have correct content")
  }

  os.Remove(file)
}
```

You can check out the full code here: https://github.com/rudylee/go-playground and please leave a comment if find any errors.
