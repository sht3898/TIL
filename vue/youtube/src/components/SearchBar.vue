<template>
  <div>
    <h1>유튜브 검색기</h1>
    <input @input="onInput" type="text"> 
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            console.log('==SearchBar==')
            console.log(event.target.value)
            // $emit(이벤트이름, 값) : 커스텀 이벤트 발생
            // 이벤트이름의 이벤트를 발생 시킴(트리거)
            this.$emit('input-change-event', event.target.value)
        }
    }
}
</script>

<style>

</style>