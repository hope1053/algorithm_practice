import Foundation

func solution(_ recordList:[String]) -> [String] {
    var nicknameDict: Dictionary = [String: String]()
    
    var answerList : [String] = []
    
    for recordSet in recordList {
        let record = recordSet.components(separatedBy: " ")
        if record[0] == "Enter" || record[0] == "Change" {
            nicknameDict[record[1]] = record[2]
        }
    }
    
    for recordSet in recordList {
        let record = recordSet.components(separatedBy: " ")
        
        // let userName = nick
        
        if record[0] == "Enter" {
            answerList.append("\(nicknameDict[String(record[1])] ?? "")님이 들어왔습니다.")
        } else if record[0] == "Leave" {
            answerList.append("\(nicknameDict[String(record[1])] ?? "")님이 나갔습니다.")
        }
    }
    
    return answerList
    
}