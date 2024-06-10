using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zombie : MonoBehaviour
{

    public float speed = 0.05f;
    public float rotationSpeed = 100.0f;
    public Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        float move = Input.GetAxis("Vertical");
        float turn = Input.GetAxis("Horizontal");

        if (move != 0){
            animator.SetBool("Walk", true);
            Vector3 movement = transform.forward * move * speed * Time.deltaTime;
            transform.position += movement;
        }
        else{
            animator.SetBool("Walk", false);
        }
        if (turn != 0 ){
            float rotation = turn * rotationSpeed * Time.deltaTime;
            transform.Rotate(0,rotation,0);
        }
    }
}
