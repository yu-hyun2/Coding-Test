function solution(n) {
    var answer = 0;
    var num = n ** (1/2)
    answer = num % 1 === 0 ? 1 : 2
        
    return answer;
}