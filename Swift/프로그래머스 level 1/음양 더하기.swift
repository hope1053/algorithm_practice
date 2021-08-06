import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var answer = 0
    for (num, value) in zip(absolutes, signs) {
        if value {
            answer += num
        } else {
            answer -= num
        }
    }
    return answer
}