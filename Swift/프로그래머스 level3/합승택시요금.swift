import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var distance = updateFare(n, fares)
    
    var minFare = Int.max
    
    for idx in 1..<n+1 {
        minFare = min(minFare, distance[s][idx] + distance[idx][a] + distance[idx][b])
    }
    
    return minFare
}

func updateFare(_ n: Int, _ fares: [[Int]]) -> [[Int]] {
    let inf = n * 100001 + 1
    
    var fareList = Array(repeating: Array(repeating: inf, count: n + 1), count: n + 1)
    
    for idx in 1..<n+1 {
        fareList[idx][idx] = 0
    }
    
    for fareInfo in fares {
        let (start, end, fare) = (fareInfo[0], fareInfo[1], fareInfo[2])
        (fareList[start][end], fareList[end][start]) = (fare, fare)
    }
    
    for k in 1..<n+1 {
        for i in 1..<n+1 {
            for j in 1..<n+1 {
                fareList[i][j] = min(fareList[i][j], fareList[i][k] + fareList[k][j])
            }
        }
    }
    
    return fareList
}