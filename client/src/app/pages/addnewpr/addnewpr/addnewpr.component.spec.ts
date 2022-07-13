import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddnewprComponent } from './addnewpr.component';

describe('AddnewprComponent', () => {
  let component: AddnewprComponent;
  let fixture: ComponentFixture<AddnewprComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddnewprComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddnewprComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
