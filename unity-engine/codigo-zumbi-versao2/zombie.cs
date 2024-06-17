using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zombie : MonoBehaviour
{
    public float speed = 0.05f;
    public float rotationSpeed = 100.0f;
    public Animator animator;

    void Start()
    {
        animator = GetComponent<Animator>();
    }

    void Update()
    {
        float move = Input.GetAxis("Vertical");
        float turn = Input.GetAxis("Horizontal");

        if (move != 0)
        {
            animator.SetBool("Walk", true);
            Vector3 movement = transform.forward * move * speed * Time.deltaTime;
            transform.position += movement;
        }
        else
        {
            animator.SetBool("Walk", false);
        }

        if (turn != 0)
        {
            float rotation = turn * rotationSpeed * Time.deltaTime;
            transform.Rotate(0, rotation, 0);
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            Attack();
        }
    }

    void Attack()
    {

        animator.SetTrigger("Attack");

    }
}
