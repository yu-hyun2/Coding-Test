function solution(a, b, flag) {
  var answer = 0;

  answer = flag === true ? a + b : a - b;

  return answer;
}
