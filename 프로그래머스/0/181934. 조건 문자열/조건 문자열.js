function solution(ineq, eq, n, m) {
  var answer = 0;

  if (ineq === '<') {
    answer = n < m;
    if (eq === '=') {
      answer = n <= m;
    }
  } else if (ineq === '>') {
    answer = n > m;
    if (eq === '=') {
      answer = n >= m;
    }
  }
  answer = answer === true ? 1 : 0;

  return answer;
}