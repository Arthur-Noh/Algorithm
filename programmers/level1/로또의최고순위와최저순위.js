// 프로그래머스
// lv. 1 / 로또의 최고 순위와 최저 순위
// JavaScript

// 문제해결아이디어

// 문제를 잘 읽어보면
// 6개의 구매한 로또 숫자를 주는데, 몇개나 맞췄는지 물어보는 문제이다. (맞춘 갯수에 따라서 등수도 정해서 리턴하면 된다.)

// 간단하게 생각해보면 된다.
// 구매한 로또와 당첨 번호를 비교하여, 맞춘 번호 배열과 못맞춘 번호 배열의 길이를 구한다.

// 가장 못 맞춘 경우는 그냥 다맞췄을 경우 6에서 맞춘 번호만 빼면 쉽게 구할 수 있다.
// 뺐는데 6 - 6 = 0 이므로 그냥 편의상 7 - 6 = 1등으로 계산한다.
// 아닌경우 그냥 7 - 맞춘 갯수

// 가장 잘 맞춘경우는 가장 못 맞춘 등수에서 알아볼 수 없는 수의 갯수를 빼주면 된다. (못한 등수에서 알수없는 수의 갯수 빼면 가장 잘한 등수가 나옴)
// 근데 뺐는데 3 - 3 = 0  이런식으로 나온경우 1등으로 간주하고,
// 아닌 경우 가장못한 등수 - 못맞춘 수의 갯수

const lottos = [44, 1, 0, 0, 31, 25];
const win_num = [31, 10, 45, 1, 6, 19];


const solution = (lottos, win_num) => {
    const numberOfPrize = lottos.filter(number => win_num.includes(number)).length;
    const numberOfDisable = lottos.filter(number => number === 0).length;
    
    let lastPrize = 7 - numberOfPrize >= 6 ? 6 : 7 - numberOfPrize;
    let firstPrize = lastPrize - numberOfDisable < 1? 1 : lastPrize - numberOfDisable;
    
    const answer = [firstPrize, lastPrize];
    
    return answer;
  
  
 console.log(solution(lottos, win_num));
