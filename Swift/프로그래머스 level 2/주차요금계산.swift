import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    var inOutRecordDict: [String: [Int]] = [:]
    
    var answerList: [(String, Int)] = []
    
    let time = 0
    let carNum = 1
    
    records.forEach {
        let inOutData = $0.components(separatedBy: " ")
        
        let inOutTime = stringToMinute(inOutData[time])
        let inOutCarNum = inOutData[carNum]
        inOutRecordDict[inOutCarNum, default: []].append(inOutTime)
    }
    
    inOutRecordDict.forEach {
        let totalFee = calculateFee($1, fees)
        
        answerList.append(($0, totalFee))
    }
    
    answerList.sort(by: {$0.0 < $1.0})
    
    return answerList.map { $0.1 }
}

func stringToMinute(_ inOutTime: String) -> Int {
    let timeData = inOutTime.components(separatedBy: ":")
    
    let hour = Int(timeData[0])!
    let minute = Int(timeData[1])!
    
    let totalMinute = hour * 60 + minute
    
    return totalMinute
}

func calculateFee(_ timeList: [Int], _ feeList: [Int]) -> Int {
    var totalFee: Int = 0
    
    var recordedTimeList = timeList
    let latestTime = 23 * 60 + 59
    
    if recordedTimeList.count % 2 == 1 {
        recordedTimeList.append(latestTime)
    }
    
    var totalTime = 0

    for idx in 0..<Int(recordedTimeList.count / 2) {
        totalTime += recordedTimeList[idx * 2 + 1] - recordedTimeList[idx * 2]
    }
    
    let basicTime = 0
    let basicFee = 1
    let additionalTime = 2
    let additionalFee = 3

    if totalTime <= feeList[basicTime] {
        totalFee = feeList[basicFee]
    } else {
        let overTimeFee = Int(ceil(Double(totalTime - feeList[basicTime]) / Double(feeList[additionalTime]))) * feeList[additionalFee]
        
        totalFee = feeList[basicFee] + overTimeFee
    }
    
    return totalFee
}