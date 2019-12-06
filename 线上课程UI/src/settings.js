export default {
  Host: 'http://127.0.0.1:8000',


  check_user_login() {
    let token = sessionStorage.user_token || localStorage.user_token;
    return token
  }
}
