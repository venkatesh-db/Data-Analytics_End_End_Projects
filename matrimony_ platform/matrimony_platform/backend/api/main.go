package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "API is up and running!")
	})

	// Start the server
	fmt.Println("Starting API server on port 8080...")
	http.ListenAndServe(":8080", nil)
}
