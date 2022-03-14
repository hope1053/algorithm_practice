import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    var answer: [Int] = Array(repeating: 0, count: id_list.count)
    
    var reportedDict: [String: Int] = [:]
    var whoReportedDict: [String: Set<String>] = [:]
    
    var overReportedList: [String] = []
    
    Set(report).forEach {
        let reporterList = $0.components(separatedBy: " ")
        
        let reporter = reporterList[0]
        let reported = reporterList[1]
        
        whoReportedDict[reporter, default: []].insert(reported)
        reportedDict[reported, default: 0] += 1
    }
    
    for (reported, count) in reportedDict {
        if count >= k {
            overReportedList.append(reported)
        }
    }
    
    for (idx, id) in id_list.enumerated() {
        let reportList = whoReportedDict[id] ?? []
        
        overReportedList.forEach {
            if reportList.contains($0) {
                answer[idx] += 1
            }
        }
    }
    
    
    return answer
}