// 프로그래머스
// lv. 1 / 신고 결과 받기
// JavaScript

// 문제해결아이디어


// 문제를 잘 읽어보면
// 1. 유저 목록을 주고
// 2. "신고한사람 신고당한사람" 이런 형식으로 리스트를 주고
// 3. k 번 이상 신고를 당하면 신고한사람 당한사람 모두에게 이메일을 준다.

// 간단하게 생각해보면 된다.
// 신고 당한 유저의 ID 를 키 값으로 하고 뒤에 [배열] 형태로 신고한 유저 수를 넣는 오브젝트를 만든다.
// 해당 오브젝트를 순회하면서 신고한 유저 수를 세고, k 보다 높다면 모든 이름 +1 하면 된다.

const id_list = ["muzi", "frodo", "apeach", "neo"];
const report = [ "muzi frodo", "apeach frodo" , "frodo neo", "muzi neo", "apeach muzi"];
const k = 2

const solution = (id_list, report, k) => {
  const result = new Array(id_list.length);  // 유저 수만큼 리스트를 만들고
  result.fill(0);  // 기본값은 0으로 채워준다.

  const reportList = {};  // 신고당한 사람의 오브젝트를 만들고
  id_list.map((user) => {
    reportList[user] = []  // 키 값은 유저 이름으로 만든다.
  });

  report.map((user) => {  // 신고 리스트를 순회하면서
    const [userId, reportId] = user.split(' ');  // 신고한 유저, 당한 유저를 띄어쓰기 ' ' 로 분리하고
    if (!reportList[reportId].includes(userId)) {  // 만약 신고가 되어있지 않다면(이미 신고한 경우를 거를려고)
      reportList[reportId].push(userId);  // 아까 만든 신고당한사람 오브젝트에 신고한 사람 이름을 넣는다.
    }
  });

  for(const key in reportList) {  // 신고당한 사람 오브젝트를 순회하면서
    if(reportList[key].length >= k) {  // K 번 이상의 사람 이름이 들어가면
      reportList[key].map((user) => {  // 유저 이름 다 찾아서
        result[id_list.indexOf(user)] += 1;  // 메일 리스트에 +1 씩 해준다.
      })
    }
  }

  return result;
}

console.log(solution(id_list, report, k));
