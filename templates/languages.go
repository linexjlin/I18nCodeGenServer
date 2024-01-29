package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

var langs_json = `{languages_json}`
var langs_data map[string]map[string]string

func UText(k string) string {
	if len(langs_data) == 0 {
		json.Unmarshal([]byte(langs_json), &langs_data)
	}
	l := os.Getenv("ULANG")
	if l == "" {
		l = "default"
	}
	if val, ok := langs_data[k]; ok {
		if v, ok := val[l]; ok {
			return v
		} else {
			fmt.Printf("Not supported lang: %v\n", l)
			go requestOnline(k, l)
		}
	} else {
		go requestOnline(k, l)
	}
	return k
}

func requestOnline(k, l string) {
	url := fmt.Sprintf("{api_addr}/{project_id}/key?k=%v&l=%v", k, l)

	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Failed to get data: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Failed to read data: %v\n", err)
		return
	}

	var result map[string]string
	json.Unmarshal(body, &result)

	return
}
