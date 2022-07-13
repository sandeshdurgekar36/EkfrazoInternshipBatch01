import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatetComponent } from './statet.component';

describe('StatetComponent', () => {
  let component: StatetComponent;
  let fixture: ComponentFixture<StatetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatetComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
