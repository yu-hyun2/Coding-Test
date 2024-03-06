function solution(a, b) {
  var answer = 0;
  var result1 = Number(String(a) + String(b));
  var result2 = Number(String(b) + String(a));

  answer = result1 > result2 ? result1 : result2;
  return answer;
}