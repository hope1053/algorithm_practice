import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var answerNumArr: [Int] = [0, 0, 0]
    var answer: [Int] = []
    let answerLength = answers.count
    
    let firstArr = [1,2,3,4,5]
    let secondArr = [2,1,2,3,2,4,2,5]
    let thirdArr = [3,3,1,1,2,2,4,4,5,5]
    
    for i in 0..<answers.count {
        if answers[i] == firstArr[i % 5] {
            answerNumArr[0] += 1
        }
        if answers[i] == secondArr[i % 8] {
            answerNumArr[1] += 1
        }
        if answers[i] == thirdArr[i % 10] {
            answerNumArr[2] += 1
        }
    }
    
    for i in 0..<3 {
        if answerNumArr[i] == answerNumArr.max() {
            answer.append(i + 1)
        }
    }
    
    return answer
}