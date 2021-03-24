<template>
  <div>
    <label>Enter your hieght:<input type="text" v-model="bmi.hieght" /></label><br/>
    <label>Enter your wieghtt:<input type="text" v-model="bmi.wieght" /></label><br/>
    <button @click="CalculateBmi">Calcualte BMI</button>
    <br/>
    <strong>{{resul}}</strong>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      bmi:{
        hieght:"",
        wieght:""
      },
      name:"",
      resul:""
    }
  },
  methods:{
    CalculateBmi(){
      axios({
        method:"post",
        url:"http://localhost:5000/bmi",
        data:{
          hieght:this.bmi.hieght,
          wieght:this.bmi.wieght,
          name:this.name
        }
      }).then((r)=>{
        this.resul=r.data.bmi
      })
    }
  },
  mounted() {
    if(sessionStorage.getItem('username')!=undefined)
    {
      this.name=sessionStorage.getItem('username')
    }
    else{
      this.$router.push("/login")
    }
  }
}
</script>
