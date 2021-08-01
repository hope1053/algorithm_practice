import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    let zippedArr = zip(a,b)
    var sum = 0
    for (c, d) in zippedArr {
        sum += c * d
    }
    return sum
}