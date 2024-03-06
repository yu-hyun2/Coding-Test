function solution(my_string, overwrite_string, s) {
  var answer = '';

  for (var i = 0; i < my_string.length; i++) {
    answer +=
      (i >= s) & (i - s < overwrite_string.length)
        ? overwrite_string[i - s]
        : my_string[i];
  }

  return answer;
}