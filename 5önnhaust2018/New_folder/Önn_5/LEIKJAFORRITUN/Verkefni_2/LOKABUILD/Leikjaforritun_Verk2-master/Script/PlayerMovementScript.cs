using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovementScript : GameManager {

    public float speed; // Gildi sem ræður hraða á player
    public float jumpForce;
    Rigidbody2D rgdbdy2d;
    SpriteRenderer spriteR;
    Animator anim;

    bool onGround = false; //Boolean sem sér hvort ég er á gólfinu eða ekki
    public Transform groundCheck; //Collider sem skoðar hvort player sé á gólfinu eða ekki
    float groundRadius = .2f; //Gildi sem segir hversu stórt groundcheck collider-inn verður
    public LayerMask WhatIsGround; //Segir Unity hvað player getur lent á
    public GameManager gm; //gm = game manager
    AudioSource[] audio; //Setur hljóðin í array og svo setur hvert og eitt hljóð í sitt eigið variable til þess að kalla á seinna
    AudioSource getHit;
    AudioSource collectGem;

    void Start () {
        rgdbdy2d = GetComponent<Rigidbody2D>(); // Finnur rigidbody sem er tengt við þetta script (sem er player)
        spriteR = GetComponent<SpriteRenderer>(); //Finnur sprite-ið sem það er að vinna með
        anim = GetComponent<Animator>(); //Finnur animator-inn í objectinu
        audio = GetComponents<AudioSource>();
        getHit = audio[0]; //Setja hljóðin í sitthvorum breytum til þess að nota þau seinna
        collectGem = audio[1];
	}


    void Update()
    {
        if (gm.gameOver) //Ef leikurinn er búinn þá leyfir þetta ekki input
            return;

        if (Input.GetButtonDown("Jump") && onGround) //Skoðar hvort við séum á gólfinu og hoppar hann
        {
            anim.SetBool("Ground", false);
            rgdbdy2d.AddRelativeForce(Vector2.up * jumpForce);
        }
    }
        
    void FixedUpdate ()
    {
        if (gm.gameOver)
            return;
        onGround = Physics2D.OverlapCircle(groundCheck.position, groundRadius, WhatIsGround); //Býr til collider á player sem segir hvort hann sé á gólfi eða ekki
        anim.SetBool("Ground", onGround);
        anim.SetBool("Dead", false);


        float horizontalMove = Input.GetAxis("Horizontal"); //Fá gildið sem stýrir hægri og vinstri

        rgdbdy2d.velocity = new Vector2(horizontalMove * speed, rgdbdy2d.velocity.y); //Hreyfa player hægri eða vinstri

        if (horizontalMove > .01) // Þetta flippar character modelinum þannig að sprite-ið snýr í rétta átt
        {
            spriteR.flipX = false;
        }
        if (horizontalMove < -.01)
        {
            spriteR.flipX = true;
        }

        anim.SetFloat("Run", Mathf.Abs(horizontalMove));

    }

    void OnTriggerEnter2D(Collider2D collision) 
    {
        if (collision.gameObject.CompareTag("Damage")) //Skoðar hvort player er búinn að snerta eitthvað sem getur meitt hann
        {
            getHit.Play();
            anim.SetBool("Dead", true); //Breytir animation-ið aftur í venjulega svo hann er ekki fastur í previous animation þegar hann dó
            rgdbdy2d.velocity = rgdbdy2d.velocity * 0; //Hættir að hreyfa player þegar hann deyr svo að þá getur hann ekki sjálfkrafa farið á meðan Game Over screen er
            transform.position = gm.Respawn.position; //Hendir player aftur á check point/respawn point
            gm.UpdateLives(-1);

        }    

        if (collision.gameObject.CompareTag("Gem")) //Ef player snertir gem þá spilar það hljóð og eyðir því út, og bætir líka svo stigi
        {
            gm.GemCount();
            collectGem.Play();
            Destroy(collision.gameObject);
        }

        if (collision.gameObject.CompareTag("Win")) //Þetta kemur þegar þú vinnur
        {
            gm.TriggerWin();
            rgdbdy2d.velocity = rgdbdy2d.velocity * 0;
        }
    }


}