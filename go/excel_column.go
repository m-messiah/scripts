package main

import "fmt"

func solution(n int) string {
    var a []byte
    if n == 0 {
        return ""
    }
    for n > 0 {
        mod := byte(n % 26)
        if mod == 0 {
            a = append([]byte{90}, a...)
            n = int(n / 26) - 1
        } else {
            a = append([]byte{mod + byte(64)}, a...)
            n /= 26
        }
    }
    return string(a)
}

func main(){
    fmt.Println(solution(0))
    fmt.Println(solution(14))
    fmt.Println(solution(134))
}