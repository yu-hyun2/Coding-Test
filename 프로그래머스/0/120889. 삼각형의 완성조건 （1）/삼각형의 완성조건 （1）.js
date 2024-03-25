function solution(sides) {
    var answer = 0;
    sides.sort();
    answer = sides[2] < sides[0] + sides[1] ? 1 : 2;
    return answer;
}