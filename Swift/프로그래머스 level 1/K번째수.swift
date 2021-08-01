import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var start: Int
    var finish: Int
    var index: Int
    var revisedArray: [Int]
    var answer: [Int] = []
    
    for command in commands {
        start = command[0]
        finish = command[1]
        index = command[2]
        revisedArray = (array[start - 1..<finish]).sorted()
        answer.append(revisedArray[index - 1])
    }
    return answer
}