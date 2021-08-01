func solution(_ n:Int, _ m:Int) -> [Int] {
    var answer: [Int] = []
    var gcd = min(n, m)
    
    while gcd > 0 {
        if n % gcd == 0 && m % gcd == 0 {
            break
        } else {
            gcd -= 1
        }
    }
    
    return [gcd, gcd * (n / gcd) * (m / gcd)]
}