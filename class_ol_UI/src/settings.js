export default {
  Host: 'http://api.feedertv.com:8000',


  check_user_login() {
    let token = sessionStorage.user_token || localStorage.user_token;
    return token
  }
}
