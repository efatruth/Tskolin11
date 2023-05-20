using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyOpossumMoveScript : MonoBehaviour
{
    public float speed;
    public Transform[] patrolPoints; // Points sem segir hvar enemy á að fara
    public Transform currentPatrolPoint; // Segir hvaða patrol point enemy er að fara núna
    public int currentPatrolPointIndex = 0; // Segir hvaða patrol point í patrolPoints-array sem enemy er að nota
    SpriteRenderer spriteR;

    void Start()
    {
        spriteR = GetComponent<SpriteRenderer>();
        currentPatrolPoint = patrolPoints[currentPatrolPointIndex];
        if (currentPatrolPoint.position.x < transform.position.x) //Ef næsta patrol point er hægri eða vinstri megin við enemy þá snýr hann við.
        {
            speed = 2f;
            spriteR.flipX = false;
        }
        else
        {
            speed = -2f;
            spriteR.flipX = true;
        }
        }


    void Update()
    {
        transform.Translate(Vector2.left * Time.deltaTime * speed); //Hreyfir enemy

        if (Vector2.Distance(currentPatrolPoint.position, transform.position) < .4f) //Ef enemy er búinn að labba framhjá patrol point
        {
            GetNextPatrolPoint();
        }


    }

    void GetNextPatrolPoint()
    {
        if (currentPatrolPointIndex < patrolPoints.Length - 1) //If-setning sem skoðar hvort það eru fleiri control points í array, annars byrjar upp á nýtt á patrol 0.
            currentPatrolPointIndex++;
        else
            currentPatrolPointIndex = 0;

        currentPatrolPoint = patrolPoints[currentPatrolPointIndex]; //Nær í næsta control point

        if (currentPatrolPoint.position.x < transform.position.x)
        {
            speed = 2f;
            spriteR.flipX = false;
        }
        else
        {
            speed = -2f;
            spriteR.flipX = true;
        }
    }

}
