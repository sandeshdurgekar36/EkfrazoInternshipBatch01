import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { StatusService } from 'src/app/services/status.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.css']
})
export class StatusComponent implements OnInit {
  

  constructor(private sService: StatusService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.statusform = new FormGroup({
      'status_name':new FormControl(null, Validators.required),
    });
  }
   get status_name() {
    return this.statusform.get('status_name');
  }
  statusform =this.fb.group({
    status_name : ['',Validators.required]
  })
  status(){
    console.log(this.statusform.value)
    this.sService.status(this.statusform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}

