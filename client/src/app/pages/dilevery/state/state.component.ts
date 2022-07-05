import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { StateService } from 'src/app/services/state.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-state',
  templateUrl: './state.component.html',
  styleUrls: ['./state.component.css']
})
export class StateComponent implements OnInit {
  

  constructor(private sService: StateService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.stateform = new FormGroup({
      
      'State_name':new FormControl(null, Validators.required),
    });
  }
    get State_name() {
    return this.stateform.get('State_name');
  }
  stateform =this.fb.group({
    state_name : ['',Validators.required]
  })
  states(){
    console.log(this.stateform.value)
    this.sService.states(this.stateform.value).subscribe(response =>{
      alert("State Added");
      console.log(response)
    })

  }
}
