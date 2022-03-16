import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    var answer: Int = 0
    
    let kNotationNum = transInToKnotation(n, k)
    let numList = kNotationNum.components(separatedBy: "0").filter { $0 != "" }
    
    numList.forEach {
        if isPrimeNum($0) {
            answer += 1
        }
    }
    return answer
}

func transInToKnotation(_ n: Int, _ k: Int) -> String {
    var totalResult = ""
    
    var (quot, remainder) = n.quotientAndRemainder(dividingBy: k)
    
    while quot > 0 || remainder > 0 {
        totalResult = "\(remainder)" + totalResult
        (quot, remainder) = quot.quotientAndRemainder(dividingBy: k)
    }
    
    return totalResult
}

func isPrimeNum(_ n: String) -> Bool {    
    let num = Int(n)!
    
    var isPrime = true
    
    if num < 3 {
        isPrime = num == 1 ? false : true
    } else {
        for division in 2...Int(sqrt(Double(num))) + 1 {
            if num % division == 0 {
                isPrime = false
                break
            }
        } 
    }
        
    return isPrime
}