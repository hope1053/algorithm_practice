import Foundation

func solution(_ s:String) -> Int {
    var numString = s
    let numDict: [String:Character] = ["zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"]

    for (key, value) in numDict {
        numString = numString.replacingOccurrences(of: String(key), with: String(value))
    }

    return Int(numString)!
}