function solution(my_string, overwrite_string, s) {
    let answer = ''
    const overLength = overwrite_string.length

    for (let index = 0 ; index < my_string.length ; index += 1){
        if (index >= s && index < s + overLength){
            answer += overwrite_string[index - s]

        } else {
            answer += my_string[index]

        }
    }
    return answer
}
