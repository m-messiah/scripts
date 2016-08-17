package main

import (
    "math"
    "os"
    "fmt"
    "strings"
    "strconv"
)

func IP2Int(ip string) int {
    var res int
    for i, octet := range strings.Split(ip, ".") {
        o, err := strconv.Atoi(octet)
        if err != nil {
            return 0
        }
        res += o * int(math.Pow(256, float64(3 - i)))
    }
    return res
}

func Int2IP(ipnum int) string {
    octets := make([]string, 4)
    for i := 3; i >= 0; i-- {
        octets[i] = strconv.Itoa(ipnum % 256)
        ipnum = ipnum / 256
    }
    return strings.Join(octets, ".")
}

func main(){
    if strings.Contains(os.Args[1], ".") {
        fmt.Println(IP2Int(os.Args[1]))
    } else {
        ipnum, err := strconv.Atoi(os.Args[1])
        if err != nil {
            fmt.Println("Bad input")
            return
        }
        fmt.Println(Int2IP(ipnum))
    }
}