import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var budget = budget
    var d = d
    var sum = 0
    var count = 0
    
    d.sort()
    
    for val in d {
        sum += val
        if sum > budget{
            break
        }
        count += 1
    }
    
    return count
}