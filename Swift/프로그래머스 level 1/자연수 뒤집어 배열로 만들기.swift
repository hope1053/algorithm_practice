func solution(_ n:Int64) -> [Int] {
    var sampleString = Array(String(String(n).reversed()))
    return sampleString.map { Int(String($0))! }
}