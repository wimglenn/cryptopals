package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"log"
)

func hexToBase64(src []byte) string {
	dst := make([]byte, hex.DecodedLen(len(src)))
	n, err := hex.Decode(dst, src)
	if err != nil {
		log.Fatal(err)
	}
	str := base64.StdEncoding.EncodeToString(dst[:n])
	return str
}

func main() {
	// Challenge 1
	src := []byte("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
	// expected := "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	str := hexToBase64(src)
	fmt.Println(str)
}
