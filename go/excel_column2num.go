package main

import (
    "fmt"
    "math"
    "strings"
)

func solution(s string) int {
    var sum int
    const uppercase string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if s == "" {
        return 0
    }
    for i, v := range s {
        sum += int(math.Pow(26, float64(len(s) - 1 - i)) * float64((strings.Index(uppercase, string(v)) + 1)))
    }
    return sum
}

func main(){
    fmt.Println(solution(""))
    fmt.Println(solution("C"))
    fmt.Println(solution("ABC"))
}