import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var answer = 0
    
    for num in left...right {
        if floor(sqrt(Double(num))) == sqrt(Double(num)) {
            answer -= num
        } else {
            answer += num
        }
    }
    
    return answer
}